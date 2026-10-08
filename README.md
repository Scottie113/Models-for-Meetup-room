# Framed Starry Night

Created in Blender 5.2. A dark walnut-colored stepped frame, satin brass trim, warm linen-colored mat, backing panel, and the painting with a brushstroke normal map.

- starry-night-framed.blend: editable scene, packed image textures, camera and lighting.
- starry-night-framed.glb: ready to import, six separate mesh parts, embedded PBR materials and both painting maps. No camera or lights included.
- frame-preview.png: Blender render.

Painting dimensions: 1.5 x 1.0 meters. Frame outer dimensions: approximately 1.846 x 1.346 meters. Scale the imported root uniformly for your scene. The GLB uses X for width and Y for height.

With Babylon.js and its glTF loader loaded:

```js
const result = await BABYLON.SceneLoader.ImportMeshAsync(
  '', '/assets/', 'starry-night-framed.glb', scene
);
const artwork = result.meshes[0];
artwork.scaling.setAll(0.6);
```

Use scene lighting and an environment texture for brass reflections. The painting already has its color and normal maps assigned. Normal mapping gives visual brushstroke relief rather than geometric displacement. Wood and mat finishes use constant PBR colors, not scanned wood grain or woven fabric textures.

The Blender render was visually checked. Import into a live Babylon.js scene has not been tested.
