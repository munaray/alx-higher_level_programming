#include "lists.h"

/**
 * createNode - This function dynamically allocate memory to the new node
 * @number: use to set the node's data.
 * Return: newNode on success.
 */

listint_t* createNode(int number) {
    listint_t* newNode = (listint_t*)malloc(sizeof(listint_t));
    if (newNode == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return NULL;
    }
    newNode->n = number;
    newNode->next = NULL;
    return newNode;
}


/**
 * insert_node - function takes a pointer to the head of the list and the
 * number to be inserted
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: NULL on failure else a pointer to the new node.
*/

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newNode = createNode(number);
    listint_t *current = *head;
    listint_t *prev = NULL;

    if (newNode == NULL)
    {
        return (NULL);
    }

    /* Traverse the list until a node with greater data is found */
    while (current != NULL && current->n < number)
    {
        prev = current;
        current = current->next;
    }
    /* If newNode is to be inserted at the beginning */
    if (prev == NULL)
    {
        newNode->next = *head;
        *head = newNode;
    }
    else
    {
        /* Insert newNode between prev and current */
        newNode->next = prev->next;
        prev->next = newNode;
    }
    return newNode;
}