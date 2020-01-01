#include "bit_stream.h"


void bit_stream_test_one() {
  BitStream bs;
  bs.Write(8, 255);
  bs.Flush();
  assert(bs.Code().size() == 1 &&
         bs.Code()[0] == (char)255);

  ReverseBitStream rbs(&(bs.Code()[0]), &(bs.Code()[0]) + bs.Code().size());
  uint32_t bits;
  bool ans = rbs.Read(8, &bits);
  assert(ans && bits == 255);
  assert(!rbs.Read(1, &bits));
}

void bit_stream_test_two() {
  int n = 5;
  uint32_t bits [] = { 0, 12, 1, 13, 2 };
  int32_t num_bits [] = { 1, 5, 2, 4, 3 };

  BitStream bs;
  for (int i = 0; i < n; i++)
    bs.Write(num_bits[i], bits[i]);
  bs.Flush();
  ReverseBitStream rbs(&(bs.Code()[0]), &(bs.Code()[0]) + bs.Code().size());
  for (int i = 0; i < n; i++) {
    uint32_t this_bits;
    bool ans = rbs.Read(num_bits[i], &this_bits);
    assert(ans);
    assert(this_bits == bits[i]);
  }
  assert(rbs.NextCode() == &(bs.Code()[0]) + bs.Code().size());
}

int main() {
  bit_stream_test_one();
  bit_stream_test_two();
  printf("Done\n");
}
