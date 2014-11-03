Title: Raspberry Lego
Status: draft
Tags: raspberryPI, Lego, python
Date: 2013-1-27

First chance to play with Pi

Lego Mindstorms

Motor to motor

![a](|filename|/images/autosave.jpeg)

[a link relative to content root](|filename|python-one-of-natures-giants.md)

> Implementing the H Bridge circuit for DC motor control on the Raspberry Pi

> The motor is powered by a 9v battery and the direction of the motor is
> controlled by the use of a H bridge. The H bridge works by the use of
> transistors T1, T2, T3 and T4. These transistors act like switches and are
> paired (T1 and T4) (T2 and T3). When current is allowed to pass through
> transistors T1 and T4, this allows the current to pass through the DC motor in
> one direction. When transistors T2 and T3 are active, this allows the current
> to flow in the opposite direction through the DC motor, reversing the
> direction.

> The control of which the Paired transistors are turned on can be done via
> tactile switches but since we are wanting to use the GPIO pins on the Raspberry
> Pi then this isn't an option, so we need to build a circuit that will interface
> and control the H bridge circuit. This where transistors T5 and T6 come into
> play. These replace where the tactile switches would be. The use of PNP
> transistors means we can place them between the 9v supply and the H Bridge as
> the load will be after them. Since being PNP they are looking for a ground in
> order for them to allow current to pass through them and onto the H bridge.

> The control of the grounding circuits for transistors T5 and T6 is done by the
> NPN transistors T7 and T8. which are in turn controlled by the GPIO pins on the
> Raspberry Pi.

> The use of LED's D1 and D2 are there for diagnostics purpose, as this give a
> visual reference to the activity on the GPIO pins.
>
>
>

> Example of use.

> When GPIO pin 14 is set to HIGH with the program (which has been written in python > with RPi.GPIO).

> Transistor T8 becomes active which in turn activates T6 thus allowing current
> to activate T2 and T3. Now with transistors T2 and T3 active, there is a
> complete circuit from the 9v battery to the DC motor.

> If GPIO pin 17 is active, transistors T7, T5, T1 and T4 become active and the
> 9v current from the battery passes through the DC motor in the opposite
> direction


