[section target]

arch: amd64
arch_desc: x86-64bit

[section portage]

CFLAGS: -march=core2 -O2 -pipe
CHOST: x86_64-pc-linux-gnu
HOSTUSE: mmx sse sse2
