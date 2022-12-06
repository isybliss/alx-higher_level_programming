#include "lists.h"

/**
 * reverse_listint - Reverse a singly linked list
 * @head: pointer to the first node
 * Return: pointer to head of reversed list
 */

listint_t reverse_listint(listint_t **head)
{
	listint_t *current = *head, *next, *prev = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (&head);
}

/**
 * is_palindrome - check if a singly linked list is palindrome
 * @head: pointer to first node
 * Return: 0 if not palindrome, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
<<<<<<< HEAD
		size++;
		tmp = tmp->next;
=======
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}

		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}

		slow = slow->next;
>>>>>>> 0772f53946fefbe81acc6102c6a2b253decf4061
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
<<<<<<< HEAD
		if (tmp->n != rev->n)
=======
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
>>>>>>> 0772f53946fefbe81acc6102c6a2b253decf4061
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}
