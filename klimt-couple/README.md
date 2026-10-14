# The Kiss-inspired posed couple

Two stylized 3D figures interpreted from the Klimt-inspired painting in this chat. The man bends his head toward the woman's temple, their arms embrace, her eyes are closed, and her folded legs and feet emerge at the side of the floral dress. Unseen anatomy and clothing are invented; the pose and likeness are approximate rather than a measured reconstruction.

## GLB files

- klimt-couple-posed.glb: both figures together, with separate Man and Woman roots.
- man-posed.glb: man alone in the same shared coordinates.
- woman-posed.glb: woman alone in the same shared coordinates.

Import the two separate files without changing their transforms to reassemble the embrace. The models use meters and glTF Y-up. Robe motifs, hair curls, flowers and hand details are actual geometry with embedded PBR material colors. No external image textures are required.

Also included: klimt-couple.blend, the editable Blender 5.2 source scene, and couple-preview.png. The studio floor, camera and lights are excluded from GLBs.

These are fixed-pose models, without skeletons or animation rigs. They are stylized rather than photorealistic. The Blender preview is checked; live Babylon.js import has not been tested.

With Babylon.js and the glTF loader available:

```js
await BABYLON.SceneLoader.ImportMeshAsync('', '/assets/', 'klimt-couple-posed.glb', scene);
```

Provide scene lighting and an environment texture for the gold materials.
