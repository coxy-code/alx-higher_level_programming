#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: pointer to the head of the linked list
* Return: 0 if no cycle, 1 if a cycle is found
*/
int check_cycle(listint_t *list)
{
listint_t *slow = list, *fast = list;

while (slow != NULL && fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;

if (slow == fast)
return (1); /* Cycle found */
}

return (0); /* No cycle */
}

