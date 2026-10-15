# Rousseau-inspired The Sleeping Gypsy

An AI-generated interpretation inspired by Henri Rousseau's The Sleeping Gypsy: a sleeping traveler in striped clothing, lion, mandolin, water jug and moonlit desert. This version adapts the composition and is not an exact reproduction of the original painting.

Included: rousseau-framed.blend (editable Blender scene, packed images), rousseau-framed.glb (assembled artwork), sand-frame-only.glb (frame and backing), rousseau-color.png, rousseau-normal.png, and frame-preview.png.

The newly designed frame has a sand-colored finish and dark blue inner lip. Frame materials use constant PBR colors, not scanned textures. Artwork dimensions: 1.5 x 1 meter. Outer frame: approximately 1.646 x 1.146 meters. GLB axes: X width, Y height, Z depth.

The painting uses an sRGB color map and linear OpenGL-style normal map with restrained paint relief. All images are embedded in the GLB. The normal map is artistically inferred and changes lighting rather than physical geometry.

With Babylon.js and its glTF loader:

```js
await BABYLON.SceneLoader.ImportMeshAsync('', '/assets/', 'rousseau-framed.glb', scene);
```

Provide scene lighting. The Blender render is visually checked; live Babylon.js import is untested.

Built-in image generation prompts: landscape Rousseau-inspired Sleeping Gypsy scene, resting adult traveler in multicolored striped robe, calm lion, mandolin and clay jug under a full moon in a desert, dreamlike simplified painted forms, no frame or text. Normal-map edit: preserve alignment, OpenGL +Y normal data, fine shallow brushstroke texture across a flat canvas, no sculpted subjects or pigment colors.
