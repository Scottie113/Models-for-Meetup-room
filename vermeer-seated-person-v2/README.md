# Seated Vermeer-inspired person — version 2

An updated stylized interpretation of the person in the painting from this chat. This version retains the stool and seated pose, with a more pronounced three-quarter head turn, slight head tilt and eyes shifted back toward the viewer. The angle is visually approximated from the painting; it is not a measured reconstruction.

Added detail includes finer facial geometry, lower eyelids, brow hairs, eye highlights, nostril and lip details, ear contours, diagonal scarf folds, a cloth knot, hem stitching, bodice and sleeve seams, elbow creases and fingernails.

- vermeer-seated-person.blend: editable Blender 5.2 scene with the full-body presentation camera.
- seated-person-with-stool.glb: complete figure and stool.
- seated-person-only.glb: the seated figure alone.
- wooden-stool.glb: separate stool.
- seated-person-preview.png: full-body render.
- portrait-detail.png: closer view of the face and headscarf.

The original version is preserved in the sibling vermeer-seated-person folder. This remains a stylized approximate likeness in a fixed pose, without an animation rig or photographic skin textures. Unseen body and clothing details are invented. Models use meters and GLB exports use Y-up. Blender renders were inspected; live Babylon.js import has not been tested.

To load with Babylon.js and its glTF loader:

```js
await BABYLON.SceneLoader.ImportMeshAsync(
  '', '/assets/', 'seated-person-with-stool.glb', scene
);
```
