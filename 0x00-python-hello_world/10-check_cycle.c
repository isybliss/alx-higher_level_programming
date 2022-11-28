#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check if a singly linked has a cycle within
 * @list: singly linked list
 * Return: 0 if there id no cycle, 1 if cycle is present
 */

int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *tail;

	if (list == NULL)
		return (0);
	head = list;
	tail = list;
	while (tail != NULL && tail->next != NULL)
	{
		head = head->next;
		tail = tail->next->next;
		if (head == tail)
			return (1);
	}
	return (0);
}
