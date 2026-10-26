---
name: adaptive-ui-checklist
description: Checklist for writing or changing any UI (Jetpack Compose or Compose Multiplatform, SwiftUI or UIKit, web) so it works on every phone size and aspect ratio, tablets, foldables (folded, unfolded, tabletop), split-screen and landscape, large font scales and long translations. Use before and after every UI change, on screens, cards, pages, dialogs, sheets and onboarding, and put the checklist result in the handoff.
---

# Adaptive UI checklist

A layout is correct only if it is correct at every size, not on the phone it was drawn on. Typical failure: a two-image collage is pinned to opposite corners of a box that fills the spare height. It looks right on a 16:9 phone, and on a 19.5:9 phone the extra height becomes a large gap between the images, because the images are sized by width and stop growing.

This skill is a short review checklist. For the platform APIs read the platform skill when one is installed (`adaptive` for Android, `edge-to-edge` for insets); this file says what to check and how to prove it.

## Rules

1. **Never pin related elements to corners of leftover space.** Do not place two related elements with opposite alignments (top-start and bottom-end) or with fractions of the free height: the distance between them then grows with the screen. Size the group from its own content (widths, aspect ratios, text), then place the group (center it, or anchor it to one edge) and let the spare room become margin. Spacing between related elements is a fixed value or derives from their own size, never from the free height.
2. **Constrain, do not stretch.** Give every flexible element a cap (max width, min and max height, `weight` plus an upper bound, `max-width`, `clamp()`). On a tablet or an unfolded foldable a phone layout that fills the window looks wrong: center the content in a bounded column or use two panes.
3. **Pick the layout from the window, not the device.** Classify the window width (compact below 600 dp, medium 600 to 840 dp, expanded 840 dp and above) and treat a short height (below about 480 dp, a phone in landscape) as its own case. Never branch on the device model or the platform name. Compose: `BoxWithConstraints`, window size class, `currentWindowAdaptiveInfo()`. SwiftUI: `horizontalSizeClass`, `verticalSizeClass`, `ViewThatFits`, `GeometryReader` only where needed. Web: container queries, media queries on the viewport, `clamp()`, `dvh`.
4. **Foldables.** Folding, unfolding and tabletop posture change the window while a screen is open: keep state in the view model or in saved state (never only in a local variable), assume no fixed orientation or size, and recompute from the constraints on every pass. Keep text, buttons and key images out of the hinge or fold area: on Android read the fold with Jetpack WindowManager (`FoldingFeature`, separating or occluding), on the web use the viewport-segments and device-posture features where the browser supports them, and in a separating fold prefer two panes with the hinge between them. A cover screen is narrow and very tall (about 23:9, 340 to 360 dp wide); an unfolded inner screen is nearly square (about 840x700 dp). Both must work. iPad multitasking (Split View, Stage Manager) gives arbitrary window sizes and is the closest iOS case.
5. **Aspect ratio range.** Phones from 16:9 (short, 320x568) to 23:9; tablets 4:3 to 3:2; unfolded folds near 1:1. Images and crops keep their aspect ratio and are never distorted or cropped differently on another size.
6. **Text.** Font scale 1.0, 1.3 and 2.0 (Dynamic Type up to the largest accessibility sizes) must not clip or overlap: rows grow, text wraps or ends with an ellipsis, no fixed height around text. Test the longest translations and the scripts you ship (Chinese, Japanese, Korean, long Spanish or German titles, 4+ digit numbers, right-to-left if supported).
7. **Insets and touch.** Edge to edge: respect status bar, display cutout, navigation bar, home indicator and rounded corners through insets, never constants. Touch targets at least 48 dp (44 pt on iOS).
8. **No hard-coded device sizes.** No `if (width == 411)`, no magic number that only fits one phone. A constant is allowed only as a cap, a minimum or the spacing between two elements.

## Sizes to check (representative, dp or pt, portrait unless noted)

| Case | Size |
| :--- | :--- |
| Small phone | 320x568, 375x667 |
| Common phones | 360x800, 390x844, 393x852, 412x915 |
| Tall phone (19.5:9) | 414x896 |
| Fold cover screen (about 23:9) | 344x882 |
| Unfolded fold, nearly square | 841x701 |
| Tablet portrait and landscape | 800x1280, 1280x800 |
| Phone landscape | 896x414, 844x390 |

Keep the list as data in one place in the tests, so a new case is one line.

## How to verify

1. **Sized tests.** A UI test that does not set the window size can pass while checking almost nothing (the default test window may clamp tall content). Set the size explicitly (Compose: `runComposeUiTest` or `runSkikoComposeUiTest` with a sized window; Android: `@Config(qualifiers = "w360dp-h800dp")` or `Modifier.size`; web: a viewport per case). Assert relations, not pixels: the gap between two related elements is at most a fixed value, nothing overlaps, nothing leaves the window, the primary action is visible. Check that the test found the nodes it should (a count), so a clamped window is noticed.
2. **Look at it.** Render the screen to an image at three sizes at least (a small phone, a tall phone, an unfolded or tablet size), before and after, and read the images. Keep the images out of the repository (scratch directory).
3. **Pure maths.** If a layout rule involves arithmetic (a group height, an overlap, a centered offset), put it in a pure function with unit tests, including the case where the box is exactly as tall as the group (nothing changes on a short phone).
4. **Devices and emulators.** Check at least one small and one tall real phone when available, and a foldable emulator (a foldable AVD, the fold-in and fold-out profiles) for a change that touches window structure. Say in the handoff what could not be checked on a device.

## Checklist for the handoff

Copy into the final message and fill in:

- [ ] No element is placed by corners of leftover space; spacing does not depend on free height.
- [ ] Every flexible element has a cap; checked on a tablet or unfolded size.
- [ ] Layout is chosen from the window constraints, not from the device.
- [ ] State survives a fold or unfold; content avoids the hinge.
- [ ] Checked at (list the sizes you ran, at least a small phone, a tall phone, a fold cover size, an unfolded or tablet size).
- [ ] Font scale 1.0, 1.3, 2.0 and the shipped languages including the longest.
- [ ] Insets and cutouts; touch targets.
- [ ] Rendered images looked at (and where they are).
- [ ] Not checked, and why.
