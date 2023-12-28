package web_dtos

type IDto interface {
	Validate() []string
}
