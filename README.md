# qubes-clip
Manage Qubes' global clipboard programmatically through Python

### How to copy files to dom0

The Qubes official documentation has information about copying files to dom0: https://www.qubes-os.org/doc/how-to-copy-from-dom0/#copying-to-dom0

For better security, you should download this into a disposable VM, to prevent a compromised qube from tampering with the data locally

For the best security, you should use [qubes-clean](https://github.com/NobodySpecial256/qubes-clean) to copy this script into dom0
