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

		# Flake Utils
		flake-utils = {
			url = "github:numtide/flake-utils";
		};

		# Nix Formatter - Alejandra
		alejandra = {
			url = "github:kamadorueda/alejandra";
			inputs.nixpkgs.follows = "nixpkgs";
		};
	};

	outputs = inputs @ {
		nixpkgs,
		lix-module,
		...
	}:
		inputs.flake-utils.lib.eachDefaultSystem (
			system: let
				pkgs = nixpkgs.legacyPackages.${system};
			in {
				formatter = inputs.alejandra.defaultPackage.${system};
				devShells.default =
					pkgs.mkShell {
						packages = with pkgs; [
							# latex
							texlab

							# python
							(python3.withPackages (ps:
										with ps; [
											# python packages here
										tkinter
											matplotlib
											numpy
											sympy
											scipy
											astropy
										]))
							basedpyright
							ruff
							uv
						];
					};
			}
		);
}
