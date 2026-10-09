# Wanderer character

A stylized, manually constructed 3D interpretation of the man in the Friedrich-inspired painting from this chat. This is not a photogrammetric reconstruction or an exact likeness. The rear-view reference informs the dark green frock coat, chestnut hair, trousers, boots, cane and raised-foot pose. The unseen face and front clothing are invented.

- wanderer-character.blend: editable Blender 5.2 scene, separate body/clothing/hair parts, lighting, camera and optional display rock.
- wanderer-character.glb: standalone static posed character with embedded PBR materials, ready for import into a 3D application. The display rock and studio are excluded.
- character-rear-preview.png and character-front-preview.png: Blender renders.

Approximately 1.8 meters tall. Export uses glTF Y-up. Materials are solid PBR colors with modeled surface details, not photographic textures. This model is not rigged or animation-ready. The raised foot is intended to rest on a rock or step. The hair is modeled as stylized locks.

With Babylon.js and its glTF loader available:

```js
const result = await BABYLON.SceneLoader.ImportMeshAsync(
  '', '/assets/', 'wanderer-character.glb', scene
);
```

Use lighting and position a rock or step under the raised left foot to complete the pose. Renders are inspected in Blender; runtime import into Babylon.js has not been tested.
