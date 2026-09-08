{ pkgs, inputs, ... }:
inputs.treefmt-nix.lib.mkWrapper pkgs {
    projectRootFile = "flake.nix";

    # nix
    programs.deadnix.enable = true;
    programs.nixfmt = {
        enable = true;
        indent = 4;
        strict = true;
    };
}
