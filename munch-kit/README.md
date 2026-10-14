# Munch-inspired The Scream

An AI-painted recreation inspired by Edvard Munch's The Scream, with a newly designed charcoal frame and warm inner trim. This is not an exact scan of the original artwork or a reproduction of its historical frame.

Included: munch-framed.blend (editable Blender scene with packed image textures), munch-framed.glb (assembled painting and frame), charcoal-frame-only.glb (frame and backing), munch-color.png, munch-normal.png, and frame-preview.png.

Painting dimensions are 0.9 x 1.2 meters; outer frame approximately 1.058 x 1.358 meters. GLB width is X, height is Y, depth is Z. Scale the imported root uniformly. Maps and PBR materials are embedded in the GLB. Color is sRGB; normal data is linear, OpenGL-style. Surface relief is AI-inferred shading, not physical displacement. The frame has solid PBR finishes rather than scanned wood grain.

With Babylon.js and its glTF loader available:

```js
await BABYLON.SceneLoader.ImportMeshAsync('', '/assets/', 'munch-framed.glb', scene);
```

Provide scene lighting. Blender render visually checked; live Babylon.js import untested.

Images generated with the built-in image generation tool. Color prompt: portrait recreation inspired by The Scream, pale foreground figure with hands at head, diagonal walkway and two distant figures, curving blue fjord, flowing orange-red sunset, expressive painted texture, no frame or text. Normal prompt: aligned OpenGL +Y tangent-space map with restrained brushstroke ridges, neutral 128/128/255 flat surfaces, no sculpted scene depth or pigment colors.
