from cffi import FFI

if __name__ == "__main__":

    rust_ffi = FFI()
    c_ffi = FFI()
    go_ffi = FFI()

    rust_ffi.cdef("""
        double add(double, double);
    """)
    c_ffi.cdef("""
        void helloworld(void);
    """)
    go_ffi.cdef("""
        double addOne(double);
    """)

    Rust = rust_ffi.dlopen(
        "C://Users//dego_//source//repos//rust//rust_deno_ffi//target//debug//rust_deno_ffi.dll"
    )
    C = c_ffi.dlopen(
        "C://Users//dego_//source//repos//c_cpp//deno_ffi//test.dll")
    Go = go_ffi.dlopen(
        "C://Users//dego_//source//repos//go//deno_ffi//deno.dll")

    print(f"hello python ffi: {Rust.add(2.2, 1.5)}")
    C.helloworld()
    print(f"Hello from Go: {Go.addOne(12.3)}")
