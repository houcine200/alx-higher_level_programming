#include  "lists.h"
/**
 * check_cycle - Check if a linked list has a cycle
 * @list: A pointer to the head of the linked list
 *
 * Description: This function determines whether a linked list contains a cycle
 *
 * Return: If there is a cycle, it returns 1. Otherwise, it returns 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;
	
	while(slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if(slow == fast)
			return (1);
	}
	return (0);
}
