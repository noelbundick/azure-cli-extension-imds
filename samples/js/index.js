const { ManagedIdentityCredential } = require('@azure/identity');

// DANGER: this dumps a Managed Identity accessToken in plain text to STDOUT
async function main() {
  const cred = new ManagedIdentityCredential();
  const token = await cred.getToken('https://management.azure.com/.default');
  console.log(JSON.stringify(token, null, 2));
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
