FROM ghcr.io/otterworks/ltib-centos:latest

LABEL org.opencontainers.image.source https://github.com/otterworks/ltib-lpc3250
LABEL org.opencontainers.image.description LTIB container for LPC3250
MAINTAINER M Jordan Stanway "m.j.stanway@alum.mit.edu"

USER root
COPY ltibrc $HOME/.ltibrc
COPY lfs-5.1 $HOME/ltib/dist/lfs-5.1
RUN chown -R ltib:ltib $HOME/ltib/dist
COPY config $HOME/ltib/config
RUN chown -R ltib:ltib $HOME/ltib/config

# put the toolchain, kernel, and new external sources directly into the LPP
WORKDIR /opt/ltib/pkgs
COPY patches/* ./
RUN curl -SLO https://cdn.kernel.org/pub/linux/kernel/v2.6/linux-2.6.27.8.tar.bz2 \
 && curl -SLO ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz \
 && curl -SLO http://ftp.gnome.org/pub/gnome/sources/glib/2.43/glib-2.43.3.tar.xz

USER ltib
WORKDIR $HOME/ltib
RUN ./ltib --preconfig config/lpc3250-base.config --batch --continue
