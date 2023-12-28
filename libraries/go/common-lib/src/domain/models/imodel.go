package domain_models

type IModel interface {
	Validate() []string
}
