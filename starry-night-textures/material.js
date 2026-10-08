// Babylon.js global build. Load after babylon.js, then call:
// mesh.material = createStarryNightMaterial(scene, './starry-night-textures/');
function createStarryNightMaterial(scene, textureFolder = './') {
  const root = textureFolder.endsWith('/') ? textureFolder : textureFolder + '/';
  const material = new BABYLON.PBRMaterial('starry-night-oil-paint', scene);
  material.albedoTexture = new BABYLON.Texture(root + 'starry-night-color.png', scene);
  material.albedoTexture.gammaSpace = true;
  material.bumpTexture = new BABYLON.Texture(root + 'starry-night-normal.png', scene);
  material.bumpTexture.gammaSpace = false;
  material.bumpTexture.level = 0.35;
  material.metallic = 0;
  material.roughness = 0.48;
  // OpenGL-style map in a default left-handed Babylon scene.
  material.invertNormalMapX = false;
  material.invertNormalMapY = false;
  for (const texture of [material.albedoTexture, material.bumpTexture]) {
    texture.wrapU = BABYLON.Texture.CLAMP_ADDRESSMODE;
    texture.wrapV = BABYLON.Texture.CLAMP_ADDRESSMODE;
    texture.anisotropicFilteringLevel = 8;
  }
  return material;
}
