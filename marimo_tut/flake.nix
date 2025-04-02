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
        python312Packages.fastparquet
        python312Packages.openpyxl
        python312Packages.watchdog
        python312Packages.duckdb
        python312Packages.polars
        python312Packages.pyarrow
        python312Packages.sqlglot
        httpfs2
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
