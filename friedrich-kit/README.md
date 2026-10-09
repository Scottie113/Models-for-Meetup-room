# Romantic-era painting and frame

AI-generated interpretation of Caspar David Friedrich's Wanderer above the Sea of Fog (1818), from the Romantic era. This is a recreation, not a scan of the original artwork. The frame is a newly designed ebonized classical molding with antique-gold accents, not a reconstruction of the historical frame.

## Files

- wanderer-framed.blend: editable Blender 5.2 scene, packed painting textures, camera and lighting.
- wanderer-framed.glb: assembled frame and painting with embedded PBR materials and image textures.
- romantic-frame-only.glb: frame and backing without the painting surface.
- wanderer-color.png: painting color texture (sRGB).
- wanderer-normal.png: inferred fine brushstroke normal map (linear, OpenGL +Y convention).
- frame-preview.png: rendered preview.

Painting: 0.9 x 1.2 meters. Outer frame: approximately 1.058 x 1.358 meters. The gold lip overlaps the painting slightly. Model width is X, height is Y and depth is Z in the GLB. Scale the imported root uniformly to fit your scene.

## Babylon.js

With Babylon.js and its glTF loader available:

```js
const result = await BABYLON.SceneLoader.ImportMeshAsync(
  '', '/assets/', 'wanderer-framed.glb', scene
);
const framedPainting = result.meshes[0];
framedPainting.scaling.setAll(0.8);
```

Painting maps are already assigned. Add scene lighting and an environment texture for gold reflections. The frame materials are solid PBR finishes, not scanned wood or gilding textures. The subtle normal map changes shading rather than adding real geometry. It is artistically inferred and not measured paint relief.

Rendered and visually checked in Blender; not runtime-tested in Babylon.js.

## Image generation

Created with the built-in image generation tool.

Color prompt: A portrait recreation inspired by Friedrich's Wanderer above the Sea of Fog: a traveler seen from behind in a dark green frock coat, cane and rocky summit, luminous mountain fog, receding blue-gray peaks, muted Romantic oil-paint palette, delicate brushwork, evenly lit, no text or frame, 3:4 aspect ratio.

Normal prompt: Convert the exact painting to an aligned OpenGL +Y tangent-space normal texture. Encode only very delicate oil-paint ridges and bristle marks, flat neutral RGB 128/128/255, no sculpted landscape, no pigment colors or baked shadows.
