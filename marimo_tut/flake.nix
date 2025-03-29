{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: 
  let
    system = "x86_64-linux";
    pkgs = import nixpkgs {
      inherit system;
    };
  in 
  {
    devShells.${system}.default = with pkgs; mkShell {
      buildInputs = [
        python312
        python312Packages.pip
        python312Packages.matplotlib
        python312Packages.numpy
        python312Packages.pandas
        pyright
        ruff
        mypy
        isort
        marimo
      ];
     
      shellHook = ''
          echo "Welcome to python  "
      '';
    };
  };
}
