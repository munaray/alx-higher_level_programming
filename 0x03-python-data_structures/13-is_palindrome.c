#include "lists.h"

/**
 * reverseList - This reverse the linked list
 * @head: pointer to the first node in the list
 *Return: pointer to the first node in the new list
 */

listint_t* reverseList(listint_t* head)
{
    listint_t *prev = NULL, *current = head, *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return (prev);
}

/**
 * isPalindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prevSlow = *head, *midNode = NULL;
    listint_t *secondHalf = reverseList(slow);
    listint_t *temp1 = *head, *temp2 = secondHalf;
    int isPalindrome = 1;
    if (*head == NULL || (*head)->next == NULL)
    {
        return 1;
    }
    /* Move fast pointer by two nodes and slow pointer by one node */
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prevSlow = slow;
        slow = slow->next;
    }
    /* Handle odd-length lists */
    if (fast != NULL)
    {
        midNode = slow;
        slow = slow->next;
    }
    /* Reverse the second half of the linked list */
    prevSlow->next = NULL;
    secondHalf = reverseList(slow);
    /* Compare the first half and reversed second half of the linked list */
    while (temp1 != NULL && temp2 != NULL)
    {
        if (temp1->n != temp2->n)
        {
            isPalindrome = 0;
            break;
        }
        temp1 = temp1->next;
        temp2 = temp2->next;
    }
    /* Restore the original list by reversing the reversed second half */
    if (midNode != NULL)
    {
        prevSlow->next = midNode;
        midNode->next = secondHalf;
    }
    else
    {
        prevSlow->next = secondHalf;
    }
    return isPalindrome;
}