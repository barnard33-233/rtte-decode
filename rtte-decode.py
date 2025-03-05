#!/usr/bin/env python3
import sys

def calculate_pa(entry):
    print("\nPA:")
    print("Level\tPA")
    mask = 0xfffffffff000
    pa = entry & mask
    # since i don't care other levels
    print(f"03\t0x{pa:016x}")


def parse_s2tte(entry):
    entry = int(entry, 16)
    
    desc_type = entry & 0b11  # DESC_TYPE [1:0]
    hipas = (entry >> 2) & 0b111  # HIPAS [4:2]
    ripas = (entry >> 5) & 0b11  # RIPAS [6:5]
    ns = (entry >> 55) & 0b1  # NS [55]
    
    print(f"s2tte\t0x{entry:016x}\n")
    print( "DESC_TYPE\tHIPAS\tRIPAS\tNS")
    print(f"0b{desc_type:02b}\t\t0b{hipas:03b}\t0b{ripas:02b}\t0b{ns:01b}")
    calculate_pa(entry)
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rtte_decode.py <s2tte_hex>")
        sys.exit(1)
    
    parse_s2tte(sys.argv[1])
