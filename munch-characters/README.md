# Three Munch-inspired figures

Three stylized character interpretations based on The Scream recreation in this chat. They use elongated forms, asymmetry, irregular contours and baked bands of painted color inspired by the artwork. They are not exact reconstructions; the small background silhouettes provide limited detail, so their unseen features are invented.

## Individual GLBs

- foreground-scream.glb: foreground figure, both hands pressed against the head, staring eyes, open oval mouth and swaying dark robe.
- distant-walker-1.glb: first narrow dark-coated walker, arms down and one foot ahead.
- distant-walker-2.glb: second dark-coated walker with a different step and head silhouette.

Each separate model is exported at its own origin. The models are in meters, with glTF Y-up. Poses are fixed; no skeletons or animations are included.

## Other files

- three-figures-arranged.glb: all three positioned with the walkers behind and to the left of the foreground figure, inspired by the painting's composition.
- munch-three-characters.blend: editable Blender 5.2 scene.
- three-figures-preview.png: group render.
- foreground-detail.png: closer foreground render.

Painted colors are baked into vertex colors and referenced by the material, requiring no external textures. Keep vertex colors enabled in the destination renderer. This approximates a painterly style through geometry and color; it does not use a screen-space brushstroke shader. The camera and studio ground are excluded from GLBs.

Blender renders visually checked. Runtime import in Babylon.js is untested. With Babylon.js and its glTF loader available:

```js
await BABYLON.SceneLoader.ImportMeshAsync('', '/assets/', 'three-figures-arranged.glb', scene);
```
