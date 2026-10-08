# Water Lilies floating-frame kit

An AI-generated interpretation inspired by Claude Monet's Water Lilies series, not an exact reproduction of one identified canvas. Created with the built-in image generation tool and framed in Blender 5.2.

## Included

- water-lilies-framed.blend: editable scene with packed textures and presentation lighting.
- water-lilies-framed.glb: assembled painting, canvas body, pale oak-colored frame, shadow gap and backing; textures embedded.
- oak-frame-only.glb: reusable frame, shadow gap and backing without the canvas.
- water-lilies-color.png: 1536 x 1024 sRGB painting texture.
- water-lilies-normal.png: 1536 x 1024 linear OpenGL-style brushstroke normal map.
- frame-preview.png: rendered Blender preview.

The painting is 1.5 x 1.0 meters. The frame is 1.6 x 1.1 meters with a 16 mm gap on each side of the canvas. The frame finish is a constant oak-colored PBR material, not a scanned wood texture. The AI-inferred normal map provides subtle lighting relief, not physical paint displacement. Painting and frame occupy X/Y with depth along Z in the exported model.

## Babylon.js

Load Babylon.js and its glTF loader, then import the assembled asset:

```js
const result = await BABYLON.SceneLoader.ImportMeshAsync(
  '', '/assets/', 'water-lilies-framed.glb', scene
);
result.meshes[0].scaling.setAll(0.6);
```

The material and textures are already assigned. Provide scene lighting and environment lighting. The preview is checked in Blender; the GLB has not been tested in a live Babylon.js scene.

## Generation prompts

Color: Full-color Monet Water Lilies-inspired oil painting, pond filling the composition, floating lily pads and pink/white blossoms, reflected willow foliage, lavender/blue/sage/teal palette, visible broken brushwork, 3:2, evenly lit, no frame or text.

Normal: Convert the exact painting to an aligned tangent-space normal map, OpenGL +Y, neutral 128/128/255 flat areas, subtle raised brushwork and bristle grooves, no sculpted scene objects or baked illumination.
