{
  description = "Python development environment using nixos-unstable";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
      in {
        devShells.default = pkgs.mkShell {
          name = "python-dev-shell";

          buildInputs = with pkgs; [
            python313
            python313Packages.jinja2
            python313Packages.pip
          ];

          shellHook = ''
            echo "🐍 Python version: $(python --version)"
          '';
        };
      });
}

