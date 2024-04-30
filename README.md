This is a repository for the development and cross-compilation environment
for a LPC3250 SoM. It uses [`podman`][podman] and [`LTIB`][ltib].

This container builds [`FROM ghcr.io/otterworks/ltib-centos:latest`][from],
which should circumvent difficulties needing `mknod` to build the `skell`
package, which requires elevated privileges.

_____________

_____________
[podman]: https://docs.podman.io
[ltib]: http://ltib.org

[from]: https://github.com/otterworks/ltib-centos
