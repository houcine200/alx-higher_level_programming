#include"lists.h"

int is_palindrome(listint_t **head);

listint_t *reverse_list(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return 1;

    // Create a copy of the original list
    listint_t *copy = NULL;
    listint_t *curr = *head;
    while (curr != NULL)
    {
        add_nodeint_end(&copy, curr->n);
        curr = curr->next;
    }
    // Reverse the copy
    listint_t *reversed = reverse_list(&copy);

    // Compare the original list with the reversed copy
    listint_t *list1 = *head;
    listint_t *list2 = reversed;

    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
        {
            listint_t *current;

            while (copy != NULL)
            {
                current = copy;
                copy = copy->next;
                free(current);
            }


            return 0; // Lists are not equal
        }
        list1 = list1->next;
        list2 = list2->next;
    }

    listint_t *current;

    while (copy != NULL)
    {
        current = copy;
        copy = copy->next;
        free(current);
    }
    return (list1 == NULL && list2 == NULL);
}
