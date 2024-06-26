FROM ghcr.io/otterworks/ltib-centos:latest

LABEL org.opencontainers.image.source https://github.com/otterworks/ltib-lpc3250
LABEL org.opencontainers.image.description LTIB container for LPC3250
MAINTAINER M Jordan Stanway "m.j.stanway@alum.mit.edu"

USER root

# put the toolchain, kernel, and new external sources directly into the LPP
WORKDIR /opt/ltib/pkgs
COPY patches/* ./
RUN curl -#SLO https://cdn.kernel.org/pub/linux/kernel/v2.6/linux-2.6.27.8.tar.bz2 \
 && curl -#SLO ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz \
 && curl -#SLO http://ftp.gnome.org/pub/gnome/sources/glib/2.43/glib-2.43.3.tar.xz \
 && md5sum linux-2.6.27.8.tar.bz2 | tee linux-2.6.27.8.tar.bz2.md5 \
 && md5sum libffi-3.2.1.tar.gz | tee libffi-3.2.1.tar.gz.md5 \
 && md5sum glib-2.43.3.tar.xz | tee glib-2.43.3.tar.xz.md5

WORKDIR /home/ltib/ltib
COPY ./ltibrc ./.ltibrc
COPY ./lfs-5.1 ./dist/lfs-5.1/
COPY ./config ./config/
RUN chown -R ltib:ltib .ltibrc \
 && chown -R ltib:ltib dist \
 && chown -R ltib:ltib config

USER ltib

RUN ./ltib --preconfig config/lpc3250-base.config --batch --no-deploy
