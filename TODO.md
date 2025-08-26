# TODO
* copy atom for smem to registers with retile (allows non-vectorized accesses to avoid bank conflicts when K < 32 K-major)
* cta size and tiling shmoo for different C/O sizes in coefs. 16 is too large for many cases
* align_1 align_4 for build_a_kernel

