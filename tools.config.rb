Config = {
    
    "network" => "tool-box",
    
    "dotnet" => {
        "image" => "mcr.microsoft.com/dotnet/sdk:latest"
    },

    "nodejs" => {
        "image" => "node:latest",
        "ports" => [5000, 5000],
        "expose" => 5000,
        "env" => ['HOST=0.0.0.0']
    },

    "python" => {
        "image" => "python:latest",
        "ports" => [8000, 8000],
        "expose" => 8000
    },

    "mssql" => {
        "name" => "mssql",
        "image" => "mcr.microsoft.com/mssql/server:latest", 
        "password" => "RuahMan2398!",
        "volumeName" => "sqlvolume"
    }
}

