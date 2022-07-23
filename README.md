This is a repository for the development and cross-compilation environment
for a LPC3250 SoM. It uses Docker and LTIB.

Unfortunately, the `skell` package in LTIB uses `mknod` to make the nodes in
the target filesystem. This causes permissions issues when building in
containers. The only way I've found to get around it is to build this
container as root, and get the `skell` package installed, then build later
layers as a normal user (or on a CI/CD runner).

Since `skell` is the package that fails to build, I've written the Dockerfile
(Containerfile) to try to build just that package first, without any others,
so that it will fail fast.
