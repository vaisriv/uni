{
	description = "uni dev-shell flake";

	inputs = {
		# Nix Packages
		nixpkgs.url = "nixpkgs/nixos-24.11";

		# Better Nix Implementation
		lix-module = {
			url = "https://git.lix.systems/lix-project/nixos-module/archive/2.91.1-1.tar.gz";
			inputs.nixpkgs.follows = "nixpkgs";
		};

		# Generic Systems for Flakes
		systems = {
			url = "github:nix-systems/default";
		};

		# Flake Utils
		flake-utils = {
			url = "github:numtide/flake-utils";
			inputs.systems.follows = "systems";
		};
	};

	outputs = {
		nixpkgs,
		flake-utils,
		...
	}:
		flake-utils.lib.eachDefaultSystem (
			system: let
				pkgs = nixpkgs.legacyPackages.${system};
			in {
				devShells.default =
					pkgs.mkShell {
						packages = with pkgs; [
							# latex
							# texliveFull
							# texlab

							# julia
							julia-bin

							# python
							(python3.withPackages (ps:
										with ps; [
											matplotlib
											numpy
										]))
							basedpyright
							ruff
						];
					};
			}
		);
}
