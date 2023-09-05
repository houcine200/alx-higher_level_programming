#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *mid = malloc(sizeof(listint_t));
	int i;

	if(!mid)
		return NULL;

	mid->n = number;

	if ((*head)->n >= number)
	{
		mid->next = *head;
		*head = mid;
		return mid;
	}
	temp = *head;

	while (temp && temp->next && temp->next->n < number)
		temp=temp->next;

	if (!temp)
	{
		free(mid);
		return NULL;
	}

	mid->next = temp->next;
	temp->next = mid;

	return mid;
}

