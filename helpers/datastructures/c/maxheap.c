#include <stdlib.h>
#include <string.h>

typedef struct {
    int *items;
    int size;
    int max_size;
} max_heap;


max_heap create_heap(int max_size)
{
    max_heap heap = {malloc(sizeof(int) * max_size), 0, max_size};
    memset(heap.items, 0, max_size * sizeof(int));
    return heap;
}

void heap_swim(max_heap *heap, int i)
{
    int temp;
    while (i > 0 && heap->items[i] > heap->items[i/2]) {
        temp = heap->items[i];
        heap->items[i] = heap->items[i/2];
        heap->items[i/2] = temp;
        i /= 2;
    }
}

void heap_push(max_heap *heap, int item)
{
    if (heap->size + 1 < heap->max_size) {
        heap->items[heap->size] = item;
        heap_swim(heap, heap->size++);
    }
}

void heap_sink(max_heap *heap, int i)
{
    int j, temp;
    while (2 * i + 1 < heap->size) {
        int j = 2 * i + 1;
        if (j + 1 < heap->size) {
            j = heap->items[j] > heap->items[j+1] ? j : j + 1;
        }
        if (heap->items[i] >= heap->items[j]) {
            return;
        }
        temp = heap->items[i];
        heap->items[i] = heap->items[j];
        heap->items[j] = temp;
        i = j;
    }
}

int heap_pop(max_heap *heap)
{
    int top, temp;
    if (heap->size <= 0) {
        return 0;
    }
    top = heap->items[0];
    temp = heap->items[0];
    heap->items[0] = heap->items[heap->size-1];
    heap->items[heap->size-1] = temp;
    heap->size -= 1;
    heap_sink(heap, 0);
    return top;
}

int heap_empty(max_heap *heap)
{
    return heap->size == 0;
}
