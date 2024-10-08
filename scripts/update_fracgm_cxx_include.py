# Copyright 2024 the FracGM authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import utils


def update_fracgm_cxx_include():
    utils.run_command("cargo install cbindgen")

    # cbindgen --config ./cbindgen.toml --crate fracgm-cxx --output include/fracgm_rust_wrapper.h
    fracgm_cxx_path = utils.get_project_root() / "fracgm-cxx"

    utils.run_command(
        "cbindgen --config ./cbindgen.toml --crate fracgm-cxx --output include/fracgm_rust_wrapper.h",
        cwd=fracgm_cxx_path,
    )


if __name__ == "__main__":
    update_fracgm_cxx_include()
    utils.get_console().print("[bold green]Done.")
