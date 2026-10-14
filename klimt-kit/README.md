# Klimt-inspired The Kiss — framed painting

An AI-painted recreation inspired by Gustav Klimt's The Kiss, paired with a newly designed square gold frame and dark inner border. It is not an exact scan or a reproduction of the painting's historical frame.

## Files

- klimt-framed.blend: editable Blender 5.2 scene with packed painting textures and presentation lights.
- klimt-framed.glb: assembled painting and frame, with embedded PBR materials and textures.
- gold-frame-only.glb: reusable frame and backing without the painting.
- klimt-color.png: sRGB color texture.
- klimt-normal.png: linear OpenGL-style normal map for shallow paint and gold-leaf relief.
- frame-preview.png: Blender render.

Painting: 1 x 1 meter. Outer frame: approximately 1.21 x 1.21 meters. GLB uses X for width, Y for height and Z for depth. Scale uniformly for your scene.

The frame uses a metallic gold material. The painting itself uses a nonmetallic color texture: its gold appearance is painted into the image, not a selectively reflective gold-leaf material. Its AI-inferred normal map changes shading, without physical displacement. The model is visually checked in Blender; live Babylon.js import is untested.

## Babylon.js

With Babylon.js and its glTF loader available:

```js
await BABYLON.SceneLoader.ImportMeshAsync('', '/assets/', 'klimt-framed.glb', scene);
```

Add scene lights and environment lighting for the metallic frame.

## Image generation

Built-in image generation prompts: square recreation inspired by The Kiss, embracing couple, geometric and floral gold robes, flowered meadow and antique gold backdrop, intricate Viennese Art Nouveau oil-paint and gold-leaf appearance, no frame or text. Normal-map edit: same aligned square composition, OpenGL +Y tangent-space RGB, shallow gold-leaf wrinkles and paint relief, no sculpted scene depth or pigment colors.
