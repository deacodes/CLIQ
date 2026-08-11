# CL★Q!

> **A tiny creative desktop for making things that feel like you. ♡**

CL★Q! is a browser-based creative editor that turns photo and video editing into a playful, desktop-inspired experience.

[![Live Demo](https://img.shields.io/badge/Live-Demo-ff69b4?style=flat-square)](https://deacodes.github.io/CL-Q/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github)](https://github.com/deacodes/CL-Q)

## Description

CL★Q! is a browser-based creative editing application designed around a cute, interactive desktop environment. Instead of presenting the user with a traditional photo or video editor, CL★Q! turns the editing process into an experience that resembles using a small, personalized computer.

The project combines photo and video editing functionality with a playful desktop-inspired interface. Different editing tools are presented as individual `.exe`-style windows, allowing users to interact with features such as the camera, preview, filters, stickers, frames, captions, and downloading as though they were applications running on a desktop.

The main purpose of CL★Q! is to make digital editing feel more creative, personal, and enjoyable. Rather than focusing only on functionality, the project treats the interface and interaction itself as part of the creative experience.

Users can capture or work with media, customize it using visual effects and decorative assets, arrange elements within the editing environment, preview the result, and export the finished creation.

The project includes several major creative features, including:

- Photo and video capture
- Live media previews
- Custom frames
- Multiple sticker packs
- Cute emoji-style stickers
- Sticker categories and tags
- Image and video filters
- Multiline captions
- Caption colour customization
- Interactive desktop-style windows
- Custom cursor effects
- Animated and immersive backgrounds
- Audio feedback and notification sounds
- Final image/video export

### ✦ Why CL★Q!?

CL★Q! is built around one simple idea: **creative software doesn't have to feel sterile.** The interface is part of the experience, with `.exe`-style windows, custom visuals, playful interactions, and an asset system designed for easy expansion.

The interface is intentionally playful and nostalgic. The `.exe` window concept gives the project the feeling of a fictional operating system built specifically for creative editing.

---

## Project Title

**CL★Q!**

The name represents the project's identity as a cute, desktop-inspired creative editor. The application is designed to feel less like conventional editing software and more like a small creative computer environment.

The project is built as a web application, allowing it to run directly inside a modern browser without requiring users to install a conventional desktop application.

---

## How the Project Works

CL★Q! is organized as a series of interactive editing stages.

The user begins by working with their media and then moves through the customization process. Different tools become available through desktop-style windows, which can be arranged around the workspace.

A typical workflow can be represented as:

```text
Capture / Select Media
        ↓
Preview and Controls
        ↓
Filters and Editing
        ↓
Customization
        ↓
Stickers + Frames + Captions
        ↓
Final Preview
        ↓
Download / Export

```

The exact contents of each step can evolve as the project develops, but the overall idea is to keep the editing process organized while maintaining the desktop metaphor.

Instead of navigating through a conventional series of forms, the user interacts with small applications inside the CL★Q! desktop.

---

## Desktop-Style Windows

One of the defining features of CL★Q! is its window-based interface.

Editing tools are represented as independent windows with `.exe`-style identities. These windows can contain different parts of the editing workflow, such as previews, sticker libraries, controls, filters, and other tools.

Movable windows are designed to follow the user's pointer naturally.

The project uses a unified movement system so that windows across different editing stages behave consistently. This prevents individual steps from having completely different dragging behaviour and helps avoid common problems such as windows teleporting when the user starts dragging them.

The intended interaction is simple:

1. The user presses on a window's title bar.
2. The current position of the window is recorded.
3. The pointer movement is measured relative to the original position.
4. The window follows the pointer.
5. The window remains inside its workspace.
6. Releasing the pointer ends the movement.

This creates a consistent interaction model across the application.

---

## Media Editing

CL★Q! is designed to work with both images and video-oriented workflows.

Media can be captured or selected and then used as the foundation for the creation.

The media is displayed through the application's preview system, allowing users to see the effects of their changes while editing.

The project aims to keep the preview and final output consistent. Changes made during editing should be represented in the final exported result rather than being limited to the interface preview.

---

## Filters

Filters allow users to change the visual appearance of their media.

The selected filter is treated as part of the current editing state and is intended to be applied to both the live preview and the final export.

For video, this is particularly important because simply applying a visual effect to an HTML element does not necessarily mean the effect will appear in the recorded video.

The final rendering pipeline therefore applies the relevant filter during frame rendering before the canvas is captured for export.

The general rendering process is:

```
Original Media
      ↓
Filter
      ↓
Frame / Layout
      ↓
Stickers
      ↓
Caption
      ↓
Final Canvas
      ↓
Preview / Export

```

This approach helps ensure that the downloaded result matches what the user sees while editing.

---

## Frames

Frames provide another way to customize the appearance of a creation.

Frames are maintained separately from stickers so that the project's asset library remains organized and easy to expand.

Frames are stored inside:

```
assets/
└── frames/

```

New frame files can be added to this directory as the project grows.

The intended asset architecture allows the website to discover available frames rather than requiring every frame to be manually written into the main application logic.

---

## Stickers

Stickers are a major component of CL★Q!.

The project supports multiple sticker collections, including themed sticker folders and cute emoji-style assets.

Sticker packs are stored separately from frames:

```
assets/
└── stickers/

```

Individual packs can then be organized into their own directories:

```
assets/
└── stickers/
    ├── cats/
    ├── cute/
    ├── emojis/
    ├── food/
    └── ...

```

This structure allows additional sticker packs to be added without having to reorganize the rest of the project.

The sticker interface contains a category/tag area and a scrollable sticker grid.

The tag area is intentionally compact so that it does not consume too much of the sticker window. When many categories are available, the tag area can scroll internally.

The sticker grid is independently scrollable, allowing users to browse large sticker collections without scrolling the entire window.

Sticker images are displayed using containment so that artwork is not unintentionally cropped.

---

## Captions

CL★Q! supports customizable captions that can be added to creations.

Captions can contain multiple lines rather than being restricted to a single line of text.

For example:

```
hello ♡
welcome to
CL★Q!

```

The caption renderer calculates the placement of each line so that multiline text remains visually grouped.

Users can also change the caption colour.

The selected caption colour is stored with the current editing state and is used when rendering the final composition.

This means that the caption shown in the preview can also appear correctly in the exported result.

---

## Custom Cursor and Visual Effects

The interface uses a custom cursor to reinforce the desktop aesthetic.

The native cursor can be hidden while the application displays its own visual cursor.

The custom cursor is purely decorative and therefore should not intercept pointer events. This allows the user to continue interacting with buttons, windows, inputs, and other interface elements normally.

The project also includes immersive visual elements such as a large background image and parallax-style movement.

The background is positioned behind the application and does not interfere with user interaction.

These effects contribute to the overall identity of CL★Q! and help make the application feel like an environment rather than a standard webpage.

---

# Installation

CL★Q! is a web application and does not require a traditional installation process.

## Quick Start

```bash
git clone https://github.com/deacodes/CL-Q.git
cd CL-Q
python3 -m http.server 8000
```

Then open **http://localhost:8000** in your browser.

> **Tip:** Don't open `index.html` directly with `file://`. CL★Q! uses browser APIs and asset loading that work correctly when served over HTTP.


The project can be downloaded or cloned from its repository and then served locally using a development server.

## Requirements

You will need:

- A modern web browser
- A local development server
- Git, if cloning the repository
- Python or Node.js for running a local server

Recommended browsers include modern versions of:

- Google Chrome
- Safari
- Microsoft Edge
- Firefox

---

## Clone the Repository

Clone the project using Git:

```
git clone https://github.com/deacodes/CL-Q.git

```

Move into the project directory:

```
cd CL-Q

```

The project should contain the main HTML file along with its CSS, JavaScript, and asset directories.

---

## Project Structure

A typical project structure is:

```
CL-Q/
│
├── index.html
│
├── css/
│   └── style.css
│
├── js/
│   └── clq.js
│
├── assets/
│   ├── frames/
│   │   ├── frame-01.png
│   │   ├── frame-02.png
│   │   └── ...
│   │
│   ├── stickers/
│   │   ├── cats/
│   │   ├── cute/
│   │   ├── emojis/
│   │   └── ...
│   │
│   ├── backgrounds/
│   └── ...
│
└── README.md

```

The exact structure may change as the project develops.

The important principle is that application code and creative assets remain separated.

---

## Running Locally

CL★Q! should **not** be opened by double-clicking `index.html`.

Opening the project directly can produce browser security errors involving `file://` URLs.

For example:

```
Fetch API cannot load file://...

```

or:

```
Unsafe attempt to load URL file://...

```

These errors occur because browsers restrict certain JavaScript requests when a webpage is loaded directly from the local filesystem.

Instead, run the project through a local HTTP server.

### Using Python

From the project directory:

```
python3 -m http.server 8000

```

Then open:

```
http://localhost:8000

```

in your browser.

### Using Node.js

If Node.js is installed, the project can also be served with:

```
npx serve .

```

Follow the local URL provided by the server.

Using a local HTTP server allows the browser to load assets through normal relative URLs.

---

# Usage

Once CL★Q! is running, open the application in your browser.

The application is designed to guide the user through the editing workflow using its desktop-style interface.

The exact interaction can change as new features are introduced, but the general process is:

### 1. Start the application

Open the CL★Q! desktop and begin the editing workflow.

### 2. Capture or select media

Use the camera/capture functionality or select the media you want to work with.

Camera functionality may require browser permission.

### 3. Preview the media

The selected media is displayed through the preview system.

### 4. Apply filters

Choose a visual filter to change the appearance of the media.

### 5. Customize the creation

Add frames, stickers, emojis, and other decorative elements.

### 6. Add captions

Enter text and customize the caption colour.

Multiline captions can be used to create more expressive layouts.

### 7. Arrange the workspace

Move supported `.exe` windows around the desktop to create a comfortable editing environment.

### 8. Review the final preview

Check the composition before exporting.

### 9. Export

Use the download/export functionality to generate the final result.

The exported media should contain the visual changes applied during the editing process.

---

# Asset Management

One of the goals of the project is to make the asset system easy to expand.

Frames and stickers are separated into different directories.

Frames should be placed in:

```
assets/frames/

```

Sticker packs should be placed in:

```
assets/stickers/

```

This means a new sticker pack can be added without modifying unrelated application code.

For example:

```
assets/stickers/
├── cats/
├── cinnamoroll/
├── cute/
├── emojis/
└── new-pack/

```

If the asset discovery system is enabled, the new pack can then become available to the website automatically.

The same principle applies to frames.

---

# Development

CL★Q! is structured around three primary layers.

## HTML

The HTML defines the structure of the application.

It contains:

- Desktop elements
- Windows
- Buttons
- Inputs
- Preview areas
- Sticker containers
- Editing controls
- Download controls

---

## CSS

The CSS controls the visual presentation of the application.

It is responsible for:

- Desktop styling
- Window appearance
- Sticker layouts
- Responsive behaviour
- Backgrounds
- Animations
- Custom cursor styling
- Typography
- Spacing
- Scroll areas
- Visual effects

Keeping CSS separate from the HTML makes it easier to adjust the visual identity without changing the application's logic.

---

## JavaScript

The JavaScript controls the application's behaviour.

This includes:

- Window movement
- Window interaction
- Media handling
- Camera functionality
- Sticker selection
- Frame selection
- Filters
- Captions
- Preview rendering
- Export
- Downloads
- Notifications
- Sound effects
- Application state

The JavaScript should avoid duplicating functionality unnecessarily.

For example, all movable windows should use the same movement system rather than separate drag implementations for each editing step.

---

# Architecture

A central design principle of CL★Q! is consistency.

The application contains many interactive features, so duplicated logic can quickly become difficult to maintain.

For example, if Step 1 and Step 2 each have separate window movement implementations, fixing a bug in one does not necessarily fix the other.

The preferred architecture is therefore to create reusable systems.

A simplified architecture looks like:

```
                    CL★Q!
                       │
          ┌────────────┼────────────┐
          │            │            │
       Interface      State      Assets
          │            │            │
      HTML/CSS      Editing      Frames
          │          State        Stickers
          │            │          Backgrounds
          │            │
          └─────── JavaScript ─────┘
                       │
                 Rendering
                       │
              ┌────────┴────────┐
              │                 │
           Preview            Export

```

The intention is for the preview and export systems to use the same underlying state and rendering rules.

---

# Performance

Because CL★Q! contains potentially large collections of stickers and frames, asset loading is an important part of the project.

Loading every asset immediately can result in unnecessary memory usage and slow initial loading.

The project can therefore benefit from techniques such as lazy loading, asset compression and loading sticker packs only when they are needed.

Large PNG files, especially transparent sticker artwork, can consume significant memory.

Where appropriate, assets can be optimized or converted into modern formats while preserving the transparency and visual quality required by the design.

The application should also avoid unnecessarily rebuilding large parts of the interface when only one element changes.

For example, selecting a sticker should update the relevant state and preview rather than rebuilding the entire sticker library.

---

# Local Files and Browser Security

A common issue when developing CL★Q! locally is attempting to use the project through a `file://` URL.

For example:

```
file:///Users/username/Downloads/CL-Q/index.html

```

This can prevent JavaScript from loading assets through `fetch()`.

The browser may report errors such as:

```
Unsafe attempt to load URL file://...

```

or:

```
Fetch API cannot load file://...

```

This is a browser security restriction rather than necessarily an issue with the asset itself.

The recommended solution is to run the project using a local server:

```
python3 -m http.server 8000

```

and then access it through:

```
http://localhost:8000

```

The same principle applies when deploying the project online: all asset paths should be relative to the application rather than tied to a particular computer.

---

# GitHub Pages

CL★Q! can be deployed as a static website because the core application runs in the browser.

When deploying to GitHub Pages, make sure the repository contains:

```
index.html
css/
js/
assets/

```

and that all asset references use relative paths.

For example:

```
fetch("./assets/asset-manifest.json");

```

is portable.

A local path such as:

```
/Users/username/Downloads/CL-Q/assets/

```

will only work on the computer where that directory exists and should never be used in the deployed version.

---

# Contributing

Contributions are welcome as the project develops.

When contributing to CL★Q!, try to preserve the project's existing visual language and architecture.

Before making a change, identify whether the functionality already exists somewhere else in the project.

If it does, it is generally better to improve or reuse the existing implementation rather than creating another independent version.

This is particularly important for systems such as:

- Window movement
- Window resizing
- Asset loading
- Preview rendering
- Filters
- Caption rendering
- Export
- Application state

For example, a new editing step should not introduce a completely separate window-dragging system if the application already has a unified one.

---

## Contribution Guidelines

When contributing:

1. Keep HTML, CSS and JavaScript responsibilities separated.
2. Reuse existing application systems where possible.
3. Avoid duplicating event listeners.
4. Avoid creating competing movement implementations.
5. Keep asset paths relative.
6. Keep frames and stickers in their appropriate directories.
7. Test changes at multiple window sizes.
8. Test both the preview and export paths when modifying rendering.
9. Check that custom visual layers do not block pointer events.
10. Test the complete workflow after major changes.

For visual changes, make sure that the interface remains usable at different window dimensions rather than only looking correct at one fixed size.

For rendering changes, verify that the exported result matches the preview.

---

# License

The license for CL★Q! has not yet been specified.

If the project is released publicly, add the chosen license here and make sure any third-party artwork, stickers, fonts, sounds, or other resources are distributed according to their respective licenses.

---

# Contact

For questions, suggestions, bug reports, or other enquiries regarding CL★Q!, contact the project maintainer through the contact information associated with the repository.

**Project repository:** https://github.com/deacodes/CL-Q

A GitHub Issue can also be used for reporting bugs or suggesting improvements.

When reporting a bug, include:

- Browser and version
- Operating system
- What you were doing when the problem occurred
- The expected behaviour
- The actual behaviour
- Any browser console errors
- Screenshots or recordings when useful

This makes it easier to reproduce and resolve problems.

---

# Project Status

CL★Q! is an actively developed project.

The interface, editing workflow, asset system and export functionality may continue to evolve as new features are added and existing systems are refined.

The current direction of the project focuses on making the creative workflow feel cohesive: the desktop interface, editing tools, asset library, preview system and export process should all feel like parts of the same application rather than separate features.

The project is also designed with future expansion in mind. New sticker packs, frames, visual effects and desktop-style tools can be added without fundamentally changing the concept of the application.

---

# Final Notes

CL★Q! is ultimately an experiment in combining functionality with personality.

It takes familiar browser technologies—HTML, CSS, JavaScript, canvas rendering, media APIs and local/static assets—and uses them to create an editing environment that feels more like a small fictional computer.

The project is intentionally cute and interactive, but the underlying goal is still to provide a reliable creative workflow.

Media should load correctly.

Windows should move smoothly.

Stickers should remain visible.

Filters should appear in the final export.

Captions should render correctly.

Assets should be easy to add.

The preview should accurately represent the final result.

And the entire application should remain enjoyable to use.

CL★Q! is built around the idea that creative software can be functional without feeling sterile, and that the interface itself can become part of the thing you're creating.

---

**CL★Q! — a tiny creative desktop for making things that feel like you. ♡**

```
