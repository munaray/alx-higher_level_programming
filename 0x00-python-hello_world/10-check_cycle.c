#include "lists.h"
/**
 * check_cycle - takes a pointer to the list of the linked list as its parameter.
 * @list: head of linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle.
*/

int check_cycle(listint_t *list)
{
    listint_t *slow, *fast;
    if (list == NULL || list->next == NULL)
    {
        /* Empty list or list with only one node */
        return (0);
    }
    slow = list;
    fast = list->next;
    while (fast != NULL && fast->next != NULL)
    {
        if (slow == fast)
        {
            /* cycle detected */
            return (1);
        }
        slow = slow->next; /* move slow pointer by one node */
        fast = fast->next->next; /* move fast pointer by two node */
    }
    /* No cycle found */
    return (0);
}