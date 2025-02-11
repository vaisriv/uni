{
	description = "uni homework shell flake";

	inputs = {
		# Nix Packages
		nixpkgs.url = "nixpkgs/nixos-24.11";

		# Better Nix Implementation - Lix
		lix-module = {
			url = "https://git.lix.systems/lix-project/nixos-module/archive/2.91.1-1.tar.gz";
			inputs.nixpkgs.follows = "nixpkgs";
		};

		# Nix Formatter - Alejandra
		alejandra = {
			url = "github:kamadorueda/alejandra";
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
							texlab

							# python
							(python3.withPackages (ps:
										with ps; [
											# python packages here
											matplotlib
											numpy
											sympy
											scipy
										]))
							basedpyright
							ruff
						];
					};
			}
		);
}
