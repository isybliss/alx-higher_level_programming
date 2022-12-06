#include "lists.h"

/**
 * reverse_listint - Reverse a singly linked list
 * @head: pointer to the first node
 * Return: pointer to head of reversed list
 */

void reverse_listint(listint_t **head)
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
}

/**
 * is_palindrome - check if a singly linked list is palindrome
 * @head: pointer to first node
 * Return: 0 if not palindrome, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *slow, *fast = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
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
	}

	reverse_listint(&dup);

	while (dup && temp)
	{
		if(temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
