package web_controllers

type IDto interface {
	Validate() []string
}
