{
	inputs = {
		# Nix Packages
		nixpkgs.url = "nixpkgs/nixos-24.11";

		# Better Nix Implementation
		lix-module = {
			url = "https://git.lix.systems/lix-project/nixos-module/archive/2.91.1-1.tar.gz";
			inputs.nixpkgs.follows = "nixpkgs";
		};

		# DevEnv Setup
		devenv = {
			url = "github:cachix/devenv";
		};
	};

	outputs = {
		self,
		nixpkgs,
		devenv,
		...
	} @ inputs: let
		system = "aarch64-linux";
		pkgs = nixpkgs.legacyPackages.${system};
	in {
		packages.${system} = {
			devenv-up = self.devShells.${system}.default.config.procfileScript;
			devenv-test = self.devShells.${system}.default.config.test;
		};

		devShells.${system}.default =
			devenv.lib.mkShell {
				inherit inputs pkgs;
				modules = [
					({
							pkgs,
							config,
							...
						}: {
							# This is your devenv configuration
							packages = with pkgs; [
								hello
								cowsay
							];

							enterShell = ''
							  hello
							'';

							processes.run.exec = "hello";
						})
				];
			};
	};
}
