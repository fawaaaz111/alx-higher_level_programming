#include "lists.h"

/**
  * check_cycle - check for a cycle in a linked list
  * @list: a list to search for
  *
  * Return: 1 if it has, 0 otherwise
  */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
