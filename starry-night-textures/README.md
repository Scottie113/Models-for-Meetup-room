# Starry Night oil-paint texture

Files: starry-night-color.png (sRGB color), starry-night-normal.png (linear tangent-space normal), material.js (Babylon.js global-build helper). Both images are 1536 x 1024.

Copy this folder into your site's public assets. Load material.js after Babylon.js, then apply:

```js
mesh.material = createStarryNightMaterial(scene, '/starry-night-textures/');
```

For an ES module project, replace BABYLON references with your @babylonjs/core imports and export the function.

The mesh needs UV coordinates. A 3:2 plane preserves the painting's proportions. Curved objects need suitable UV unwrapping; this image preserves the whole painting and is not seamless. Both textures must use identical UV transforms. Default glTF UV orientation may require setting invertY consistently on BOTH texture constructors.

Use a directional or point light at an angle to reveal the brushwork, plus your scene's environment lighting. Start with bumpTexture.level = 0.35; try 0.15–0.65. Roughness 0.48 gives subdued oil-paint highlights; increase toward 0.7 for matte paint. If the vertical relief looks inverted in your scene, toggle material.invertNormalMapY.

The normal map is AI-inferred artistic relief, not measured paint geometry or guaranteed pixel-perfect reconstruction. It changes shading only, without silhouette displacement or true brushstroke shadows. The color image retains some painted/baked shading. The generated maps were visually inspected; this helper has not been runtime-tested in your Babylon.js scene.

Generated with the built-in image generation tool. Prompt: Convert the supplied painting into a tangent-space normal map, OpenGL +Y, preserving its composition and brushstroke directions; flat canvas with fine raised oil-paint ridges, no scene-depth sculpting, labels, borders, or baked lighting.

Babylon.js PBR reference: https://doc.babylonjs.com/features/featuresDeepDive/materials/using/masterPBR
