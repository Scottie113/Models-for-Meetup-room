# Vermeer-inspired framed painting

An AI-painted interpretation of Johannes Vermeer's Girl with a Pearl Earring, with a newly designed mahogany-colored frame and antique-gold trim. This is not an exact scan or a reconstruction of the original frame.

## Included

- vermeer-framed.blend: editable Blender scene, packed image textures, camera and lighting.
- vermeer-framed.glb: painting and frame with embedded PBR materials and textures.
- mahogany-frame-only.glb: reusable frame and backing without the painting.
- vermeer-color.png: sRGB painting color image.
- vermeer-normal.png: linear tangent-space normal map for subtle paint surface relief.
- frame-preview.png: Blender render.

Painting dimensions are 0.9 x 1.2 meters; outer frame approximately 1.058 x 1.358 meters. GLB width is X, height is Y, and depth is Z. Scale the imported root uniformly for your scene.

Frame materials use constant PBR finishes, not scanned wood grain. The normal map is AI-inferred surface detail and affects shading only, without true displacement.

## Babylon.js

Load Babylon.js and its glTF loader, then:

```js
const result = await BABYLON.SceneLoader.ImportMeshAsync(
  '', '/assets/', 'vermeer-framed.glb', scene
);
```

Provide scene lights and environment lighting for the gold highlights. All painting maps are already assigned. The Blender render is visually checked; live Babylon.js import is untested.

## Generation

Built-in image generation was used for both maps. Color prompt: a close painted recreation inspired by Girl with a Pearl Earring, blue and yellow headscarf, luminous face and pearl, ochre jacket, dark green-black background, delicate Dutch Golden Age oil paint texture, portrait 3:4, no frame or text. Normal prompt: convert the image into an aligned OpenGL +Y tangent-space map, subtle fine paint ridges, neutral flat RGB 128/128/255, no sculpted face or pigment colors.
