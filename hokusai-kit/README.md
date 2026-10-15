# Hokusai-inspired Great Wave

An AI-generated recreation inspired by Katsushika Hokusai's The Great Wave off Kanagawa, framed in dark wood-colored molding with an ivory mat and muted bronze trim. This is not an exact scan: it omits the original lettering and interprets the print's composition.

Files: hokusai-framed.blend (editable Blender scene with packed textures), hokusai-framed.glb (assembled artwork), dark-frame-only.glb (frame, mat and backing), hokusai-color.png (sRGB color), hokusai-normal.png (linear paper-grain normal map), and frame-preview.png.

Artwork: 1.5 x 1.0 meters. Outer frame: approximately 1.846 x 1.346 meters. GLB width is X, height Y, depth Z. Scale uniformly to fit your scene.

The print uses a matte material and very low-strength paper-grain normal map. The normal map is an artistic approximation and does not add physical displacement. Frame materials use constant PBR colors, not scanned wood textures. Image textures are embedded in the GLB.

With Babylon.js and its glTF loader available:

```js
await BABYLON.SceneLoader.ImportMeshAsync('', '/assets/', 'hokusai-framed.glb', scene);
```

Provide scene lighting. Blender render visually checked; live Babylon.js import is untested.

Built-in image generation prompts: a 3:2 Great Wave-inspired ukiyo-e print with indigo curling wave, white foam, three slender boats, distant Mount Fuji and beige sky, flat layered pigment and fine paper grain, no lettering or frame. Normal edit: nearly flat OpenGL +Y RGB normal data with microscopic paper fibers, no embossed scene contours or impasto.
